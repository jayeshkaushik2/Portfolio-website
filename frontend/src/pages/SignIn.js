import React, { useEffect, useState } from 'react'
import '../assests/SignIn.css'
import defaultProfile from '../assests/defaultProfile.png'

const SignIn = () => {

    const [profileImage, setprofileImage] = useState(null);
    useEffect(() => {
        getProfileImage()
    }, []);
    

    let getProfileImage = async () => {
        let response = await fetch('/api/get-profile/')
        let data = await response.json()
        setprofileImage(data["profile_image"])
        
    }

    return (
        <>
            <div className="container-signin">
                <div className="sign-in-form">
                    <div className="header" id="loginHeader">
                        <img src={profileImage? profileImage : defaultProfile } className="profileidimg" alt="profileidimage" />
                    </div>

                    <h6>Admin Login</h6>
                    <div className="form">
                        <div className="form-input">
                            <input className="form-control" type="email" placeholder="Email" aria-label="default input example" />
                        </div>
                        <div className="form-input">
                            <input className="form-control" type="password" placeholder="Password" aria-label="default input example" />
                        </div>

                        <div className="form-input adj">
                            <a href="#" className="btn btn-danger left Btns">forgot password?</a>
                            <button className="btn btn-primary right Btns">Sign In</button>
                        </div>

                    </div>
                </div>
            </div>
        </>
    )
}

export default SignIn
