export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      const numberOfDepartments = Object.keys(employeesList);
      return numberOfDepartments.length;
    },
  };
}
