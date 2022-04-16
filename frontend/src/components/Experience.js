import React from 'react'
import '../assests/Experience.css'
import avtarForCompany from '../assests/avtarForCompany.png'

export default function Experience() {
    return (
        <>
            <div id="ExperienceDiv">
                <p id="experienceText">Experience</p>
                <div id="schoolDiv">
                    <img src={avtarForCompany} id="defaultImg" alt="default school" />

                    <div id="content">
                        <h6>Full Stack Developer</h6>
                        <p id="score">Small bag delivery . Internship</p>
                        <p>oct 2021 - present</p>
                    </div>
                </div>
            </div>
        </>
    )
}
