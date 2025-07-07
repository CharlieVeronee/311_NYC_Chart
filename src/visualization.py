import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
import logging
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar

logger = logging.getLogger(__name__)

def plot_311(gdf, boroughs_geojson, title="NYC 311 Noise Map", save_dir=None):
    if gdf.empty:
        print("No datapoints match your filters.")
        return

    #select WebMercator coordinate system
    gdf_Mercator = gdf.to_crs(epsg=3857)
    boroughs_Mercator = gpd.read_file(boroughs_geojson).to_crs(epsg=3857)

    #establish plot
    fig, ax = plt.subplots(figsize=(12, 12))

    #base boroughs
    boroughs_Mercator.plot(ax=ax, facecolor="none", edgecolor="grey", linewidth=0.8, zorder=2)

    #basemap underneath boroughs
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, zoom=12, alpha=0.5)

    #hex‐bin heatmap of incident density
    x = gdf_Mercator.geometry.x.values
    y = gdf_Mercator.geometry.y.values
    hb = ax.hexbin(x, y, gridsize=100, mincnt=1, cmap="Reds",alpha=0.6, zorder=4)
    fig.colorbar(hb, ax=ax, shrink=0.6, label="Incidents per bin")

    #data points plotted
    gdf_Mercator.plot(ax=ax, markersize=5, color="black", alpha=0.3, marker=".", zorder=5)

    #scale bar
    ax.add_artist(ScaleBar(1, location="lower right", color="#b32400"))

    ax.set_title(title, fontsize=18, pad=20)
    ax.set_axis_off()
    plt.tight_layout()

    if save_dir:
        out_path = Path(save_dir) / f"{title.replace(' ','_')}.png"
        fig.savefig(out_path, dpi=300)
        logger.info(f"Map saved to {out_path}")
    else:
        plt.show()

    plt.show()