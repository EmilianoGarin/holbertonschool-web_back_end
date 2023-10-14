export default function updateStudentGradeByCity(listStudents, cityString, newGrades) {
  const studentsByCity = listStudents
    .filter((student) => student.location === cityString)
    .map((data) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === data.id);
      const grade = matchingGrade ? matchingGrade.grade : 'N/A';
      return { ...data, grade };
    });
  return studentsByCity;
}
