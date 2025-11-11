"""
Auto-generated Manim scene for EconViz Local.

Run:
    manim -pqh demand-and-supply-20251026124847.py EconScene  # preview
    manim -p -r 1920,1080 -q h demand-and-supply-20251026124847.py EconScene  # full quality
"""
from manim import *
import numpy as np

BEATS = [
  {
    "t_start": 0,
    "t_end": 3,
    "action": "SHOW_LINE",
    "params": {
      "name": "DEMAND"
    },
    "narration": "Baseline demand curve appears."
  },
  {
    "t_start": 3,
    "t_end": 6,
    "action": "SHOW_LINE",
    "params": {
      "name": "SUPPLY"
    },
    "narration": "Supply enters to show equilibrium."
  },
  {
    "t_start": 6,
    "t_end": 10,
    "action": "HIGHLIGHT_EQUILIBRIUM",
    "params": {},
    "narration": "Equilibrium point pulsates."
  },
  {
    "t_start": 10,
    "t_end": 16,
    "action": "MOVE_LINE",
    "params": {
      "name": "DEMAND",
      "delta_shift": -1.2,
      "delta_slope": 0.0
    },
    "narration": "Demand shifts left to show a negative shock."
  },
  {
    "t_start": 16,
    "t_end": 22,
    "action": "ADD_LABEL",
    "params": {
      "x": 3.0,
      "y": 7.5,
      "text": "Lower Q, lower P"
    },
    "narration": "Annotate the new equilibrium with lower price and quantity."
  }
]
# To load beats from JSON instead:
# import json
# with open('demand-and-supply-20251026124847.json', 'r', encoding='utf-8') as fh:
#     BEATS = json.load(fh)

LABEL_POSITIONS = []

def axes_with_labels():
    axes = Axes(
        x_range=[0, 10, 1],
        y_range=[0, 10, 1],
        x_length=9,
        y_length=5,
        axis_config={"include_tip": True},
    )
    x_label = Text("Quantity", font_size=40, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.4)
    y_label = Text("Price", font_size=40, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.4)
    labels = VGroup(x_label, y_label)
    return axes, labels

def build_line(axes, start, end, color):
    return Line(axes.c2p(*start), axes.c2p(*end), color=color, stroke_width=6)

def apply_move(line, axes, delta_slope=0.0, delta_shift=0.0):
    start = axes.p2c(line.get_start())
    end = axes.p2c(line.get_end())
    base_dx = max(end[0] - start[0], 1e-3)
    slope = (end[1] - start[1]) / base_dx
    slope += delta_slope
    new_start = (start[0], start[1] + delta_shift)
    new_end = (end[0], new_start[1] + slope * base_dx)
    return build_line(axes, new_start, new_end, line.color)

def reserve_label_position(point):
    for _ in range(3):
        collision = False
        for other in LABEL_POSITIONS:
            if np.linalg.norm(other - point[:2]) < 0.6:
                collision = True
                point += np.array([0.2, 0.2, 0])
                break
        if not collision:
            break
    LABEL_POSITIONS.append(point[:2])
    return point

def add_label(scene, axes, text, x, y):
    txt = Text(text, font_size=36, color=BLACK)
    bg = SurroundingRectangle(txt, color=GRAY, buff=0.15, fill_opacity=0.05)
    group = VGroup(bg, txt)
    target = reserve_label_position(np.array(axes.c2p(x, y)))
    group.move_to(target)
    scene.play(FadeIn(group, shift=UP * 0.2), run_time=0.8)

def highlight_equilibrium(scene, axes):
    eq_point = axes.c2p(5, 5)
    dot = Dot(eq_point, color=YELLOW, radius=0.08)
    dashed_h = DashedLine(axes.c2p(0, 5), axes.c2p(10, 5), color=YELLOW_D)
    dashed_v = DashedLine(axes.c2p(5, 0), axes.c2p(5, 10), color=YELLOW_D)
    scene.play(FadeIn(dot), Create(dashed_h), Create(dashed_v), run_time=1.2)
    scene.play(Indicate(dot), run_time=1.0)

class EconScene(Scene):
    def construct(self):
        config.frame_rate = 30
        config.pixel_width = 1920
        config.pixel_height = 1080
        config.background_color = WHITE
        axes, labels = axes_with_labels()
        self.play(Create(axes), FadeIn(labels), run_time=1.5)
        supply = build_line(axes, (0, 1), (10, 9), BLUE)
        demand = build_line(axes, (0, 9), (10, 1), RED)
        lines = {"SUPPLY": supply, "DEMAND": demand}

        for beat in BEATS:
            duration = max(0.2, beat["t_end"] - beat["t_start"])
            action = beat["action"]
            params = beat.get("params", {})
            if action == "SHOW_LINE":
                line_name = params.get("name", "").upper()
                line = lines.get(line_name)
                if line:
                    self.play(Create(line), run_time=duration)
            elif action == "MOVE_LINE":
                line_name = params.get("name", "").upper()
                line = lines.get(line_name)
                if line:
                    updated = apply_move(
                        line,
                        axes,
                        delta_slope=params.get("delta_slope", 0.0),
                        delta_shift=params.get("delta_shift", 0.0),
                    )
                    self.play(Transform(line, updated), run_time=duration)
            elif action == "ADD_LABEL":
                add_label(
                    self,
                    axes,
                    params.get("text", "Label"),
                    params.get("x", 5.0),
                    params.get("y", 5.0),
                )
            elif action == "HIGHLIGHT_EQUILIBRIUM":
                highlight_equilibrium(self, axes)
            self.wait(0.1)
