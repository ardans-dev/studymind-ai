import { useEffect, useState } from "react";
import { Folder } from "lucide-react";

import { WorkspaceAPI } from "../../services/api";
import type { Workspace } from "../../types/workspace";
import { useWorkspace } from "../../context/WorkspaceContext";

export default function Sidebar() {

    const { workspace, setWorkspace } = useWorkspace();

    const [workspaces, setWorkspaces] = useState<Workspace[]>([]);

    async function load() {
    const data = await WorkspaceAPI.list();
    setWorkspaces(data);
}

    async function createWorkspace() {
        const name = prompt("Nama Workspace");

        if (!name) return;

        await WorkspaceAPI.create(name);

        load();
    }

    useEffect(() => {
        load();
    }, []);

    return (
        <aside className="w-72 bg-slate-900 text-white flex flex-col">

            <div className="p-6">
                <h1 className="text-2xl font-bold">
                    📚 StudyMind AI
                </h1>
            </div>

            <div className="flex-1 p-4">

                <button
                    onClick={createWorkspace}
                    className="w-full bg-blue-600 rounded-lg p-3 mb-5 hover:bg-blue-700"
                >
                    + New Workspace
                </button>

                {workspaces.map((ws) => (

                    <button
                        key={ws.id}
                        onClick={() => setWorkspace(ws)}
                        className={`flex items-center gap-3 w-full rounded-lg p-3 transition ${
                            workspace?.id === ws.id
                                ? "bg-blue-600"
                                : "hover:bg-slate-800"
                        }`}
                    >
                        <Folder size={18} />
                        {ws.name}
                    </button>

                ))}

            </div>

        </aside>
    );
}