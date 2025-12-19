from pathlib import Path

BASE_DIR = Path("data_1218")
OUTPUTS = {
    "step2_ASta": Path("htc/data_1218_step2_ASta_dg20_rep1.txt"),
    "step2_ZalaZone": Path("htc/data_1218_step2_ZalaZone_dg20_rep1.txt"),
}
DIMENSIONS = range(20)
REP_VALUE = 0


def list_dataset_files(subdir: str) -> list[str]:
    folder = BASE_DIR / subdir
    return sorted([p.name for p in folder.iterdir() if p.is_file()])


def write_manifest(subdir: str, output_path: Path) -> None:
    filenames = list_dataset_files(subdir)
    lines = []
    for dg in DIMENSIONS:
        for name in filenames:
            tag = f"{subdir}_{name}".replace("/", "_")
            lines.append(f"{subdir}/{name} {dg} {REP_VALUE} {tag}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + ("\n" if lines else ""))


if __name__ == "__main__":
    for subdir, output_path in OUTPUTS.items():
        write_manifest(subdir, output_path)
