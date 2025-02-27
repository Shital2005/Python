class Student:
    @staticmethod
    def get_personal_detail(firstname,lastname):
        print("your details:",firstname,lastname)

    @staticmethod
    def contact_detail(mobile_no,roll_no):
        print("your contact details:",mobile_no,roll_no)    
        
Student.get_personal_detail('Arjun','Reddy')
Student.contact_detail(9999999999,101)