import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import './App.css'
// pages of frontend
import Homepage from "./pages/Homepage";
import Post from "./pages/Post";
import SignIn from "./pages/SignIn";
import AddPost from "./components/AddPost";

// admin pages
import { AdminPage } from "./Adminpages/AdminPage";
// import { AdminProfile } from "./Admincomponents/AdminProfile";
// import { AdminAbout } from "./Admincomponents/AdminAbout";
// import { AdminSocialLinks } from "./Admincomponents/AdminSocialLinks";
// import { AdminEducation } from "./Admincomponents/AdminEducation";
// import { AdminExperiance } from "./Admincomponents/AdminExperiance";
// import { AdminSkills } from "./Admincomponents/AdminSkills";
// import { AdminProjects } from "./Admincomponents/AdminProjects";
// import { AdminPosts } from "./Admincomponents/AdminPosts";
// import { AdminCertificates } from "./Admincomponents/AdminCertificates";
// import { AdminBody } from "./Admincomponents/AdminBody";

function App() {
  return (
    <BrowserRouter>
      <>
        <div className="App">
          <Routes>

            <Route path="/" exact element={<Homepage />} />
            <Route path="/post/:id" element={<Post />} />
            <Route path="/signin" element={<SignIn />} />
            <Route path="/addpost" element={<AddPost />} />
            <Route path="/admin" element={<AdminPage name="admin" />} />

            <Route exact path="/admin-profile" element={<AdminPage name="profile" />} />
            <Route exact path="/admin-about" element={<AdminPage name="about" />} />
            <Route exact path="/admin-sociallinks" element={<AdminPage name="sociallinks" />} />
            <Route exact path="/admin-education" element={<AdminPage name="education" />} />
            <Route exact path="/admin-experiance" element={<AdminPage name="experiance" />} />
            <Route exact path="/admin-skills" element={<AdminPage name="skills" />} />
            <Route exact path="/admin-projects" element={<AdminPage name="projects" />} />
            <Route exact path="/admin-posts" element={<AdminPage name="posts" />} />
            <Route exact path="/admin-certificates" element={<AdminPage name="certificates" />} />

            {/* <Route exact path="/admin-profile" element={<AdminProfile />} /> */}
            {/* <Route exact path="/admin-about" element={<AdminAbout />} />
            <Route exact path="/admin-sociallinks" element={<AdminSocialLinks />} />
            <Route exact path="/admin-education" element={<AdminEducation />} />
            <Route exact path="/admin-experiance" element={<AdminExperiance />} />
            <Route exact path="/admin-skills" element={<AdminSkills />} />
            <Route exact path="/admin-projects" element={<AdminProjects />} />
            <Route exact path="/admin-posts" element={<AdminPosts />} />
            <Route exact path="/admin-certificates" element={<AdminCertificates />} /> */}

          </Routes>

        </div>

      </>
    </BrowserRouter>
  );
}

export default App;
