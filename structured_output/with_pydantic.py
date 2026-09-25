from langchain_groq import ChatGroq
from pydantic import BaseModel, EmailStr, Field 
from dotenv import load_dotenv
from typing import Optional,Annotated, Literal



load_dotenv()

# create the model
model = ChatGroq(model = "openai/gpt-oss-120b")

# define the Schema
class ResumeChecker(BaseModel):
    name : str = 'Unknown'
    email : EmailStr

    skills : Annotated[
        list[str], 
        "Extract all important technical and soft skills from the resume"] 
    
    experience : Annotated[
        Literal["Entry Level", "Mid Level" , "Senior Level"], 
        "Classify the Candidate's Experience level"]
    
    expected_salary : Annotated[int ,Field(
        gt=0, 
        description="Expected Annual Salary of the candidate if mentioned in resume")] 
    
    weakness : Annotated[Optional[
        list[str]], 
        "List the candidate's possible weaknesses or ares for improvement"] = None
    

# define the structure
structured_output = model.with_structured_output(ResumeChecker)

# Inovoke the model
response = structured_output.invoke(
"""
    PARTHO KUMAR MONDAL
    Full-Stack Web Developer

    Email: parthokumarmondal90@gmail.com

    TECHNICAL SKILLS

    Frontend:
    React.js, Next.js, TypeScript, JavaScript, HTML5, CSS3, Tailwind CSS, Shadcn/ui, React Hook Form

    State Management:
    Redux Toolkit, RTK Query, Context API

    Backend:
    Python, Django, Django REST Framework

    Database:
    PostgreSQL, SQLite, MySQL, Basic MongoDB

    Authentication and Security:
    JWT Authentication, Djoser, SimpleJWT, Google OAuth, django-allauth, dj-rest-auth, Email Verification, Password Reset, Role-Based Access Control

    API and Integrations:
    REST APIs, Axios, Cloudinary, SSLCommerz Payment Gateway

    Next.js:
    Server-Side Rendering (SSR), Client-Side Rendering (CSR), Incremental Static Regeneration (ISR), Dynamic Metadata

    Tools:
    Git, GitHub, VS Code, Postman, Swagger, Vercel

    Other Skills:
    Debugging, Performance Optimization, Responsive Web Design, API Integration, Figma-to-React, Cross-Browser Development, Clean Code, Problem Solving

    i am expecting salary around 150000
"""
)

print(response)







