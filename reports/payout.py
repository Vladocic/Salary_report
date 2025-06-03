from reports.base import BaseReport

class PayoutReport(BaseReport):
    def generate(self, data:dict) -> dict: 
        for department, info in data.items():
            total_hours = 0
            total_payout = 0

            for employee in info["employees"]:
                hours = employee.get("hours", 0)
                rate = employee.get("rate", 0)
                payout = hours * rate
                employee["payout"] = f"${payout}"
                total_hours += hours
                total_payout += payout

            data[department]["total_hours"] = total_hours
            data[department]["total_payout"] = f"${total_payout}"
        return data
    
    def print_report(self, data: dict) -> None:
        print(f"{'':<20} {'name':<20} {'hours':<6} {'rate':<6} {'payout':<8}")
        for department, info in data.items():
            print(department)
            for employee in info["employees"]:
                print(f"{'-'*20} {employee['name']:<20} {employee['hours']:<6} {employee['rate']:<6} {employee['payout']:<8}")
            print(f"{'':<41} {info['total_hours']:<6} {'':<6} {info['total_payout']}" )


