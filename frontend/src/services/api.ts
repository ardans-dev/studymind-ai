import axios from "axios";

export const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const WorkspaceAPI = {

    async list() {

        const res = await api.get("/workspace");

        return res.data;

    },

    async create(name: string) {

        const res = await api.post("/workspace", null, {

            params: { name }

        });

        return res.data;

    },

    async upload(file: File) {

        const formData = new FormData();

        formData.append("file", file);

        const res = await api.post("/upload", formData, {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        });

        return res.data;

    },

};

export const DocumentAPI = {

    async list(workspaceId: string) {

        const res = await api.get(`/document/${workspaceId}`);

        return res.data;

    }

}

export const UploadAPI = {

    async upload(workspaceId: string, file: File) {

        const form = new FormData();

        form.append("file", file);

        const res = await api.post(

            `/workspace/${workspaceId}/upload`,

            form,

            {

                headers: {

                    "Content-Type": "multipart/form-data"

                }

            }

        );

        return res.data;

    }

}