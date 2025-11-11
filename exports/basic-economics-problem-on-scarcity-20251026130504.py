"""
Auto-generated Manim scene for EconViz Local.

Run:
    manim -pqh basic-economics-problem-on-scarcity-20251026130504.py EconScene  # preview
    manim -p -r 1920,1080 -q h basic-economics-problem-on-scarcity-20251026130504.py EconScene  # full quality
"""
from manim import *
import numpy as np

BEATS = [
  {
    "t_start": 0.0,
    "t_end": 15.0,
    "action": "SHOW_LINE",
    "params": {
      "line_type": "DEMAND"
    },
    "narration": "Every day, we make choices about what we want and how much we're willing to pay. This represents the demand for goods and services."
  },
  {
    "t_start": 15.0,
    "t_end": 30.0,
    "action": "SHOW_LINE",
    "params": {
      "line_type": "SUPPLY"
    },
    "narration": "On the other side, producers decide what to offer and at what price. This is the supply available in the market."
  },
  {
    "t_start": 30.0,
    "t_end": 45.0,
    "action": "HIGHLIGHT_EQUILIBRIUM",
    "params": {},
    "narration": "Where demand meets supply, we find the market equilibrium \u2013 the price and quantity where buyers and sellers generally agree."
  },
  {
    "t_start": 45.0,
    "t_end": 65.0,
    "action": "MOVE_LINE",
    "params": {
      "line_type": "SUPPLY",
      "direction": "LEFT"
    },
    "narration": "But what if a resource is limited, or a product becomes incredibly popular? This is where scarcity comes in. Let's imagine a sharp reduction in supply."
  },
  {
    "t_start": 65.0,
    "t_end": 85.0,
    "action": "ADD_LABEL",
    "params": {
      "label_text": "Shortage",
      "position": "BELOW_NEW_EQUILIBRIUM"
    },
    "narration": "Now, at the original price, demand far exceeds the available supply, creating a significant shortage. Many people want the item, but there isn't enough."
  },
  {
    "t_start": 85.0,
    "t_end": 110.0,
    "action": "ADD_LABEL",
    "params": {
      "label_text": "Scarcity: Unlimited Wants, Limited Resources",
      "position": "CENTER"
    },
    "narration": "Scarcity is the fundamental economic problem: our wants are virtually unlimited, but the resources and goods available to satisfy them are not. This forces us to make choices and drives prices up in competitive markets."
  }
]
# To load beats from JSON instead:
# import json
# with open('basic-economics-problem-on-scarcity-20251026130504.json', 'r', encoding='utf-8') as fh:
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
