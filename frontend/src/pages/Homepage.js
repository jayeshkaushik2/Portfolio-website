import React, { useEffect, useState } from 'react'
import About from '../components/About'
import SocialLinks from '../components/SocialLinks'
import ProfileHeader from '../components/ProfieHeader'
import Posts from '../components/Posts'
import LikesViewsProjects from '../components/LikesViewsProjects'
import Education from '../components/Education'
import Experience from '../components/Experience'
import SkillsAndProject from '../components/SkillsAndProject'

function Homepage() {
    const [profileDetails, setprofileDetails] = useState([]);
    const [socailLinkDetails, setSocailLinkDetails] = useState([]);
    const [educationDetails, setEducationDetails] = useState([]);

    // Getting the profile details
    useEffect(() => {
        getProfileDetails()
        getSocailLinkDetails()
        getEducationDetails()
    }, []);

    let getProfileDetails = async () => {
        let response = await fetch('/api/get-profile/')
        let data = await response.json()
        console.log("profile details:", data)
        setprofileDetails(data)
    }

    let getSocailLinkDetails = async () => {
        let response = await fetch('/api/get-sociallinks/')
        let data = await response.json()
        console.log("social links details:", data)
        setSocailLinkDetails(data)
    }

    let getEducationDetails = async () => {
        let response = await fetch('/api/get-education/')
        let data = await response.json()
        console.log("education details:", data)
        setEducationDetails(data)
    }

    return (
        <>
            <ProfileHeader profileDetails={profileDetails} />

            <LikesViewsProjects />

            <About about={profileDetails["about_user"]} />

            <SocialLinks socailLinkDetails={socailLinkDetails} />
            
            <Education educationDetails={educationDetails} />

            <Experience />

            <SkillsAndProject />

            <Posts />
        </>
    )
}

export default Homepage