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

    // Getting the profile details
    useEffect(() => {
        getProfileDetails()
    }, []);

    let getProfileDetails = async () => {
        let response = await fetch('/api/getprofile/')
        let data = await response.json()
        console.log("profile details:", data)
        setprofileDetails(data)
    }

    return (
        <>
            <ProfileHeader profileDetails={profileDetails} />

            <LikesViewsProjects />

            <About about={profileDetails["about_user"]} />

            <SocialLinks />

            <Education />

            <Experience />

            <SkillsAndProject />

            <Posts />
        </>
    )
}

export default Homepage