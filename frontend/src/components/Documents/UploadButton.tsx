import { Upload } from "lucide-react";
import { WorkspaceAPI } from "../../services/api";

export default function UploadButton() {

    async function uploadFile(
        event: React.ChangeEvent<HTMLInputElement>
    ) {

        const file = event.target.files?.[0];

        if (!file) return;

        try {

            const result = await WorkspaceAPI.upload(file);

            console.log(result);

            alert("Upload berhasil 🎉");

        }

        catch (err) {

            console.error(err);

            alert("Upload gagal");

        }

    }

    return (

        <label className="flex items-center justify-center gap-2 w-full bg-blue-600 text-white rounded-lg p-3 cursor-pointer hover:bg-blue-700">

            <Upload size={18} />

            Upload File

            <input
                type="file"
                hidden
                onChange={uploadFile}
                accept=".pdf"
            />

        </label>

    );

}