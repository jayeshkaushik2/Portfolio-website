import React from 'react'
import { Link } from 'react-router-dom'

export const AdminNavBar = () => {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <span className="navbar-brand">Admin</span>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/admin-profile">Profile</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-sociallinks">SocialLinks</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-education">Education</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-experiance">Experiance</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-skills">Skills</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-projects">Projects</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-posts">Posts</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/admin-certificates">Certifications</Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )
}
