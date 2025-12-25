class Employee:
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id

    def get_info(self) -> str:
        return f"employee: {self.name}, id: {self.emp_id}"


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self, project_name: str) -> str:
        return f"manager {self.name} manages project '{project_name}' in department {self.department}"

    def get_info(self) -> str:
        return f"manager: {self.name}, id: {self.emp_id}, department: {self.department}"


class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, equipment: str) -> str:
        return (f"technician {self.name} (specialization: {self.specialization}) "
                f"maintains equipment: {equipment}")

    def get_info(self) -> str:
        return f"technician: {self.name}, id: {self.emp_id}, specialization: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self._team = []  # list of subordinate employees

    def add_employee(self, employee: Employee) -> str:
        self._team.append(employee)
        return f"employee {employee.name} added to {self.name}'s team"

    def get_team_info(self) -> str:
        if not self._team:
            return f"{self.name} has no subordinates yet."

        result = [f"tech manager {self.name}'s team:"]
        for emp in self._team:
            result.append(" - " + emp.get_info())
        return "\n".join(result)

    # we can override get_info one more time
    def get_info(self) -> str:
        return (f"tech manager: {self.name}, id: {self.emp_id}, department: {self.department}, "
                f"specialization: {self.specialization}")


# demonstration of how it works
if __name__ == "__main__":
    # 1. regular employee
    e1 = Employee("Petr ivanov", 101)
    print(e1.get_info())
    print()

    # 2. manager
    m1 = Manager("Yakov manishek", 201, "sales department")
    print(m1.get_info())
    print(m1.manage_project("client base expansion"))
    print()

    # 3. technician
    t1 = Technician("Albina seksova", 301, "network equipment")
    print(t1.get_info())
    print(t1.perform_maintenance("cisco router"))
    print()

    # 4. tech manager (multiple inheritance)
    tm1 = TechManager("Damn khardikov", 401, "it department", "servers and databases")
    print(tm1.get_info())
    print(tm1.manage_project("migration to a new server"))
    print(tm1.perform_maintenance("postgresql database server"))
    print()

    # 5. adding employees
    print(tm1.add_employee(e1))
    print(tm1.add_employee(m1))
    print(tm1.add_employee(t1))
    print()

    # 6. printing team info
    print(tm1.get_team_info())
