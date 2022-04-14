import React from 'react'
import '../assests/SkillsAndProject.css'

export default function SkillsAndProject() {

    function myFunction() {
        var dots = document.getElementById("dots1");
        var moreText = document.getElementById("remainDescription");
        var btnText = document.getElementById("seeDescriptionBtn");

        if (dots.style.display === "none") {
            dots.style.display = "inline";
            btnText.innerHTML = "see more";
            moreText.style.display = "none";
        } else {
            dots.style.display = "none";
            btnText.innerHTML = "see less";
            moreText.style.display = "inline";
        }
    }

    return (
        <>
            <div id="SkillsAndProjectDiv">
                <div>
                    <p id="skillsandprojectText">Skills & Projects</p>
                    <h6>Python (programming language)</h6>
                    <h6>Java</h6>
                </div>

                <hr />

                <div>
                    <h6>1) Todos List</h6>
                    <span id="projectDate">Sep 2021</span>

                    <div id="description">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas vitae scel<span id="dots1">...</span><span id="remainDescription">erisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. In at libero sed nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh tempor porta.</span>
                        <button onClick={myFunction} className="showBtn" id="seeDescriptionBtn">see more</button>
                        </p>
                        <a className="link-primary" href="#" id="projectLink">See project</a>
                    </div>
                </div>
            </div>
        </>
    )
}
