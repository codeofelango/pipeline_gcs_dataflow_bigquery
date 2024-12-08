function transform(line) {
  // Split the line into an array of values using the comma as a delimiter.
  var values = line.split(',');
  
  // Create an object to store the parsed data.
  var obj = new Object();

  // Assign the values from the array to the corresponding properties of the object.
  obj.id = values[0];
  obj.name = values[1];
  obj.age = values[2];

  // Convert the object into a JSON string.
  var jsonString = JSON.stringify(obj);
  
  // Return the JSON string.
  return jsonString;
}
