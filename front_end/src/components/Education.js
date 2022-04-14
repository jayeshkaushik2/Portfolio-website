import React from 'react'
import '../assests/Education.css'
import avtar from '../assests/avtar.png'

export default function Education() {
    return (
        <>
            <div id="EducationDiv">
                <p id="EducationText">Education</p>
                <div id="schoolDiv">
                    <img src={avtar} id="defaultImg" alt="default school" />
                    
                    <div id="content">
                        <h6>Sat kabir institute of technology and management</h6>
                        <p id="score">B.tech, computer science, 7.5</p>
                        <p>2019 - 2024</p>
                    </div>
                </div>
                <div id="schoolDiv">
                    <img src={avtar} id="defaultImg" alt="default school" />
                    
                    <div id="content">
                        <h6>Marigold public school</h6>
                        <p id="score">12th, science, 75%</p>
                        <p>2018 - 2019</p>
                    </div>
                </div>
            </div>
        </>
    )
}
