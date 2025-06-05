const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Salam, Al Eye server işləyir!');
});

app.listen(port, () => {
  console.log(`Server işə düşdü: http://localhost:${port}`);
});