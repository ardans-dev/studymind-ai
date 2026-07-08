import { createContext, useContext, useState } from "react";
import type { Workspace } from "../types/workspace";

interface WorkspaceContextType {
  workspace: Workspace | null;
  setWorkspace: (workspace: Workspace) => void;
}

const WorkspaceContext = createContext<WorkspaceContextType>({
  workspace: null,
  setWorkspace: () => {},
});

export function WorkspaceProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [workspace, setWorkspace] = useState<Workspace | null>(null);

  return (
    <WorkspaceContext.Provider
      value={{ workspace, setWorkspace }}
    >
      {children}
    </WorkspaceContext.Provider>
  );
}

export function useWorkspace() {
  return useContext(WorkspaceContext);
}