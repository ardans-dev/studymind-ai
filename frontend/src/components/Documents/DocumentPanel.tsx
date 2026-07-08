import { FileText } from "lucide-react";
import { useWorkspace } from "../../context/WorkspaceContext";
import UploadButton from "./UploadButton";

export default function DocumentPanel() {

    const { workspace } = useWorkspace();

    return (

        <aside className="w-64 border-r bg-slate-50 flex flex-col">

            <div className="p-4 border-b">

                <h2 className="font-semibold text-lg">
                    {workspace ? workspace.name : "Documents"}
                </h2>

            </div>

            <div className="flex-1 p-3 space-y-2">

                <div className="flex items-center gap-2 p-2 rounded hover:bg-slate-200 cursor-pointer">
                    <FileText size={18} />
                    CNN.pdf
                </div>

                <div className="flex items-center gap-2 p-2 rounded hover:bg-slate-200 cursor-pointer">
                    <FileText size={18} />
                    GAN.pdf
                </div>

            </div>

            <div className="p-4 border-t">
                <UploadButton />
            </div>

        </aside>

    );

}