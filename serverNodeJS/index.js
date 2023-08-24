const express = require("express");
const cors = require("cors");
const sequelize = require("./db");
const router = require("./routes/index");
const models = require("./models/models");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.use("/api", router);
const start = async () => {
  try {
    await sequelize.authenticate();
    await sequelize.sync();
    app.listen(
      PORT,
      console.log(`Server is started succesfully on port ${PORT}`)
    );
  } catch (e) {
    console.log(e);
  }
};
start();