import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  for (const product of listProducts) {
    if (product.itemId === id) {
      return product;
    }
  }
  return null;
}

function reserveStockById(itemid, stock) {
  client.set(itemid, stock);
}

async function getCurrentReservedStockById(itemId) {
  return getAsync(itemId);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));

  if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    const resItem = {
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
      currentQuantity: stock !== null ? parseInt(stock) : item.initialAvailableQuantity,
    };
    res.json(resItem);
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  let stock = await getCurrentReservedStockById(itemId);
  if (!stock) {
    stock = parseInt(stock);
    if (stock > 0) {
      reserveStockById(itemId, stock - 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'not enough stock avaliable', itemId });
    }
  } else {
    reserveStockById(itemId, item.initialAvailableQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.listen(port, () => {
  console.log('Favour is the Best Software Engineer and Penetration tester in the World');
});
