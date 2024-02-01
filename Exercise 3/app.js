// app.js
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname));
// app.use(express.urlencoded({extended:true}))
// app.get("/",(req,res)=>{
//   res.sendFile('D:/Exercise 3/index.html')
// })
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
