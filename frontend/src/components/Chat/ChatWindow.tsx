import { useState } from "react";

import ChatInput from "./ChatInput";
import MessageBubble from "./MessageBubble";
import { useWorkspace } from "../../context/WorkspaceContext";

import type { Message } from "../../types/chat";

export default function ChatWindow() {

  const { workspace } = useWorkspace();

  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Halo 👋 Upload materi lalu tanyakan apa saja."
    }
  ]);

  function sendMessage(text: string) {
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: text
      }
    ]);
  }

  return (
    <div className="flex flex-col h-full">

      {/* Header */}
      <div className="border-b p-4 bg-white">

        <h2 className="text-xl font-bold">
          {workspace ? workspace.name : "Pilih Workspace"}
        </h2>

      </div>

      {/* Area Chat */}
      <div className="flex-1 overflow-y-auto p-6">

        {messages.map((msg, index) => (
          <MessageBubble
            key={index}
            message={msg}
          />
        ))}

      </div>

      {/* Input */}
      <ChatInput onSend={sendMessage} />

    </div>
  );
}