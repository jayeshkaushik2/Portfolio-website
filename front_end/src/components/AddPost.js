import React from 'react';
import '../assests/AddPost.css'

const AddPost = () => {
    return (
        <>
            <div className="container" id="AddPostDiv">
                <p id="AddPostText">Add a post</p>
                <div className="input-group mb-3">
                    <span className="input-group-text" id="basic-addon1">Title</span>
                    <input type="text" className="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" />
                </div>
                <div className="form-floating">
                    <textarea className="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
                    <label for="floatingTextarea">Description</label>
                </div>
                <div className="mb-3">
                    <label for="formFileMultiple" className="form-label">Upload Image</label>
                    <input className="form-control" type="file" id="formFileMultiple" multiple />
                </div>
            </div>
        </>
    )
};

export default AddPost;