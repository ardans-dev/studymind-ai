import ChatWindow from "../components/Chat/ChatWindow";
import DocumentPanel from "../components/Documents/DocumentPanel";

export default function Home() {

    console.log("HOME DIRENDER");

    return (
        <div className="flex h-full bg-gray-100">

            <div className="flex-1">
                <ChatWindow />
            </div>

            <DocumentPanel />

        </div>
    );

}