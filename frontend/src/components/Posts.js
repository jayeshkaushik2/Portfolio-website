import React, { useState } from 'react'
import '../assests/Posts.css'
import Post from '../pages/Post'
import { Link } from 'react-router-dom'


export default function Posts(props) {
    const [Photo, setPhoto] = useState(false);

    function profileView(index) {
        let img = document.getElementById(`${index}`)
        let ViewPost = document.getElementById(`${index}`)

        if (Photo) {
            setPhoto(false)
            console.log("this is True here!!!")
            img.style.opacity = "1"
            ViewPost.style.display = "none"
        }
        else {
            setPhoto(true)
            img.style.opacity = "0.5"
            ViewPost.style.display = "block"
        }
    }

    return (
        <>
            <div id="postsDiv">
                <p id="postText">Posts</p>
                {props.posts ? props.posts.map((post, index) => (

                    <div className="postdiv" key={index}>
                        <div className="heading">
                            <h6 className="title"> {props.posts[index]["post_title"]} </h6>
                        </div>
                        <div className="postimageDiv">
                            <Link to={"/post/" + post.id} className="link-primary viewPostLink" id={index} element={<Post />}>View Post</Link>
                            <img src={props.posts[index]["post_image"]} onClick={profileView} className="postimage" alt="postImg" id={index} />
                        </div>
                    </div>

                )) : ""}

                <button className="btn btn-primary" id="loadMore">load more</button>
            </div>
        </>
    )
}
