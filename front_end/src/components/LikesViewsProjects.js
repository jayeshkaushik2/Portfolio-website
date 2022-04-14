import React from 'react'
import '../assests/LikesViewsProjects.css'

export default function LikesViewsProjects() {
    return (
        <div>
            <div id="LikesViewsProjectsDiv">
                <div className="row" id="rowForLink">
                    <div className="col" id="columns"> <span id="spans">140</span> <i className="fa fa-thumbs-up"></i> Likes</div>
                    <div className="col" id="midColumn"> <span id="spans">41</span> <i className='fa fa-image'></i> Posts</div>
                    <div className="col" id="columns"> <span id="spans">20</span> <i className='fa fa-folder-open'></i> Projects</div>
                </div>
            </div>
        </div>
    )
}
