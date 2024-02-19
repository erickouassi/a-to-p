import { Episode } from "@/app/types";
import EpisodeDetailsPoller from "./EpisodeDetailsPoller";
import { backendClient } from "@/app/clients";

async function getEpisode(episodeId: string): Promise<Episode> {
  const response = await backendClient.GET("/api/episode/{id}", {
    params: {
      path: {
        id: episodeId,
      },
    },
    cache: "no-cache",
  });
  if (response.data) {
    return response.data;
  } else {
    throw new Error("No episode found");
  }
}
export default async function EpisodeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  const data = await getEpisode(params.id);
  return <EpisodeDetailsPoller episode={data} />;
}
