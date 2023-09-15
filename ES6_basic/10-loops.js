export default function appendToEachArrayValue(array, appendString) {
  const nArray = [];
  for (let value of array) {
    nArray.push(appendString + value);
  }

  return nArray;
}
