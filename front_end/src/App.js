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

          </Routes>

        </div>

      </>
    </BrowserRouter>
  );
}

export default App;
