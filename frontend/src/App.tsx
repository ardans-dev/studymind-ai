import Sidebar from "./components/Sidebar/Sidebar";
import Home from "./pages/Home";

function App() {
  return (
    <div className="flex h-screen">
      <Sidebar />

      <main className="flex-1 overflow-hidden">
        <Home />
      </main>
    </div>
  );
}

export default App;