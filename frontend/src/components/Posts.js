import React, { useEffect, useState } from 'react'
import '../assests/Posts.css'
import Post from '../pages/Post'
import { Link } from 'react-router-dom'


export default function Posts() {
    const [Posts, setPosts] = useState([])

    useEffect(() => {
        getPosts()
    }, [])

    let getPosts = async () => {
        let response = await fetch('/api/getposts/')
        let data = await response.json()
        console.log('Data:', data)
        setPosts(data)
    }

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
                    {Posts.map((post, index) => (

                            <div className="postdiv" key={index}>
                                <div className="heading">
                                    <h6 className="title">{post.post_title}</h6>
                                </div>
                                <div className="postimageDiv">
                                    <Link to={"/post/" + post.id} className="link-primary viewPostLink" id={index} element={<Post />}>View Post</Link>
                                    <img src={post.post_image} onClick={profileView} className="postimage" alt="postImg" id={index} />
                                </div>
                            </div>

                    ))}

                <button className="btn btn-primary" id="loadMore">load more</button>
            </div>
            {/* <div className="col" id="columns" key={index}>
                    <div className="card">

                        <Link to={"/post/"+post.id} className="link-primary centeredLink" id={index} element={<Post />}>View Post</Link>

                        <img src={post.post_image} className="card-img-top postPhoto" onClick={profileView} alt="postImg" id={index} />
                            <div className="card-body">
                                <h5 className="card-title"> {post.post_title} </h5>
                                <p className="card-text"> {post.post_description} {post.post_date} </p>
                            </div>
                        </div>
                    </div> */}

        </>
    )
}
