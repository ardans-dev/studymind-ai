import { useState } from "react";

interface Props {
  onSend: (message: string) => void;
}

export default function ChatInput({ onSend }: Props) {
  const [text, setText] = useState("");

  function handleSend() {
    if (!text.trim()) return;

    onSend(text);
    setText("");
  }

  return (
    <div className="flex gap-3 p-4 border-t">

      <input
        className="flex-1 border rounded-lg px-4 py-3"
        placeholder="Tanyakan sesuatu..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleSend();
        }}
      />

      <button
        onClick={handleSend}
        className="bg-blue-600 text-white px-5 rounded-lg"
      >
        Kirim
      </button>

    </div>
  );
}