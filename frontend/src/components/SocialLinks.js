import React from 'react'
import '../assests/SocialLinks.css'

export default function SocialLinksDiv() {
    return (
        <>
            <div id="SocialLinksDiv">
                <p id="p">
                <i className="fa fa-envelope"></i> Email: <a id="aLink" className="link-dark"> jayeshkaushik2@gmail.com </a>
                </p>
                <p id="p">
                <i className="fa fa-linkedin-square"></i> LinkedIn: <a id="aLink" target="_blank" className="link-primary" href="https://www.linkedin.com/in/jayesh-kaushik-07013a1a4/"> linkedin.com/in/jayesh-kaushik-07013a1a4 </a>
                </p>
                <p id="p">
                <i className="fa fa-github"></i> GitHub: <a id="aLink" target="_blank" className="link-primary" href="https://github.com/jayeshkaushik2/"> github.com/jayeshkaushik2 </a>
                </p>
                <p id="p">
                <i className="fa fa-code"></i> Leetcode: <a id="aLink" target="_blank" className="link-primary" href="https://leetcode.com/jayesh_kaushik/"> leetcode.com/jayesh_kaushik </a>
                </p>
            </div>
        </>
    )
}
