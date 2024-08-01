db = db.getSiblingDB('testdb');
db.testcollection.insertMany([
  { "value": 1 },
  { "value": 2 },
  { "value": 3 },
  { "value": 4 },
  { "value": 5 }
]);
