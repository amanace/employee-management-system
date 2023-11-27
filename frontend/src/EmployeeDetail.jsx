import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'



function EmployeeDetail() {
    const {id} = useParams();
    const navigate = useNavigate()
    const [employee, setEmployee] = useState([])
    
    useEffect(()=> {
        axios.get(`http://localhost:8081/employeedetail/${id}`)
        .then(res => {
            const result = res.data.Result[0];
            console.log(result);
            setEmployee(result);
          });
    })
    const handleLogout = () => {
		axios.get('http://localhost:8081/logout')
		.then(res => {
			navigate('/start')
		}).catch(err => console.log(err));
	}

  
    const buttonStyle = {
      backgroundColor: 'green',
      color: 'white',
      // Add other styles as needed
    };
  return (
    <div>
        <div className='d-flex justify-content-center flex-column align-items-center mt-3'>
            <img src={`http://localhost:8081/images/`+'ss.jpg'} alt="" className='empImg'/>
            <div className='d-flex align-items-center flex-column mt-5'>
                <h3>Name: {employee.name}</h3>
                <h3>Registraion: {employee.id}</h3>
                <h3>Email: {employee.email}</h3>
                <h3>Role: {employee.role}</h3>
                <h3>Salary: {employee.salary}</h3>
            </div>
            {/* <div>
            <button className='btn btn' style={buttonStyle} onClick={handleLogout}>Leave request</button>
            </div>
            <br></br> */}
            <div>
                <button className='btn btn-danger' onClick={handleLogout}>Logout</button>
            </div>
        </div>
    </div>
  )
}

export default EmployeeDetail