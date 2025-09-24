from pydantic import BaseModel



class StudentForm(BaseModel):
    _name : str = ''
    _age : int
    _contact : int
    _tenGrade:int
    _twelveGrade:int
    _degreeGrade:int
    _university_institute:str
    _projects:str
    _certifications:str
    _technical_skills:str
    _areas_of_interest:str
    _hobbies:str
    _extracurricular:str
    

    
