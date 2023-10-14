export default function getStudentIdsSum(listStudents) {
  const idsOfStudents = listStudents.map((idFinder) => idFinder.id);
  const idsSummed = idsOfStudents.reduce((acum, actualNumber) => acum + actualNumber, 0);
  return idsSummed;
}
