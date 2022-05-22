import React, { useState, useEffect } from 'react'

export const AdminProfile = () => {
    const [profileData, setprofileData] = useState(null)

    const [User, setUser] = useState("")
    const [Name, setName] = useState("")
    const [Profile_image, setProfile_image] = useState("")
    const [Backprofile_image, setBackprofile_image] = useState("")
    const [About_user, setAbout_user] = useState("")
    const [Profession, setProfession] = useState("")

    useEffect(() => {
        getProfileData()
    }, []);

    let getProfileData = async () => {
        let response = await fetch('/api/get-profile/')
        let data = await response.json()
        console.log("profile data:", data)
        setprofileData(data)
        setUser(data["user"])
        setName(data["name"])
        setProfile_image(data["profile_image"])
        setBackprofile_image(data["backprofile_image"])
        setAbout_user(data["about_user"])
        setProfession(data["profession"])
    }

    let postProfileData = async (data) => {
        console.log("data", data)
        let requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'multipart/form-data' },
            body: JSON.stringify(data)
        };
        let response = await fetch('/api/get-profile/', requestOptions);
        let response_data = await response.json();
        setprofileData(response_data)
        getProfileData()
    }

    const submitProfileData = (e) => {
        e.preventDefault()
        console.log("submiting..", e.target.files)
        let data = {
                user: User,
                name: Name,
                profile_image: Profile_image,
                backprofile_image: Backprofile_image,
                about_user: About_user,
                profession: Profession,
            }
        postProfileData(data)
        console.log(profileData)
    }

    return (
        <div className="container">
            <form>
                <div className="input-group flex-nowrap my-3">
                    <span className="input-group-text" id="addon-wrapping">Name</span>
                    <input type="text" className="form-control" placeholder="Name" aria-label="name" value={Name} aria-describedby="addon-wrapping" onChange={(e) => setName(e.target.value)} />
                </div>

                <div className="input-group mb-3">
                    <label className="input-group-text" htmlFor="inputGroupFile01">Upload Profile Image</label>
                    <input type="file" className="form-control" id="inputGroupFile01" onChange={(e) => setProfile_image(e.target.files[0])} />
                </div>

                <div className="input-group mb-3">
                    <label className="input-group-text" htmlFor="inputGroupFile01">Upload Backgroud Image</label>
                    <input type="file" className="form-control" id="inputGroupFile01" onChange={(e) => setBackprofile_image(e.target.files[0])} />
                </div>

                <div className="input-group mb-3">
                    <span className="input-group-text">About</span>
                    <textarea className="form-control" aria-label="With textarea" value={About_user} onChange={(e) => setAbout_user(e.target.value)} ></textarea>
                </div>

                <div className="input-group mb-3">
                    <span className="input-group-text" id="basic-addon1">Profession</span>
                    <input type="text" className="form-control" placeholder="Profession" aria-label="profession" aria-describedby="basic-addon1" value={Profession} onChange={(e) => setProfession(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-primary" onClick={submitProfileData}>Submit</button>
            </form>
        </div>
    )
}
