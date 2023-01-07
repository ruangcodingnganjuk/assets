process.on("uncaughtException", function (err) {
  console.error(new Date().toUTCString() + " uncaughtException:", err.message);
  console.error(err.stack);
  process.exit(1);
});

const express = require("express");
const app = express();
const bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/login", (req, res) => {
  res.send(`
  <html>
  <body>
    <form action="/login" method="post">
      <label for="username">Username:</label><br>
      <input type="text" id="username" name="username"><br>
      <label for="password">Password:</label><br>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Submit">
    </form> 
  </body>
  </html>
  `);
});

app.post("/login", (req, res) => {
  res.send(
    "Username: " + req.body.username + " Password: " + req.body.password
  );
});

app.listen(3000, () => {
  console.log("Server listening on port 3000");
});
