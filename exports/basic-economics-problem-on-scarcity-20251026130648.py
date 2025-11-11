"""
Auto-generated Manim scene for EconViz Local.

Run:
    manim -pqh basic-economics-problem-on-scarcity-20251026130648.py EconScene  # preview
    manim -p -r 1920,1080 -q h basic-economics-problem-on-scarcity-20251026130648.py EconScene  # full quality
"""
from manim import *
import numpy as np
import textwrap

BEATS = [
  {
    "t_start": 0.0,
    "t_end": 15.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "Scarcity: The fundamental economic problem of having seemingly unlimited human wants and needs in a world of limited resources.",
      "position": "center"
    },
    "narration": "Scarcity is the core challenge in economics. It's about our endless desires clashing with finite resources."
  },
  {
    "t_start": 16.0,
    "t_end": 35.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "Think about it: Time, money, natural resources \u2013 all are limited. But our desires for goods, services, and experiences are endless.",
      "position": "top_left"
    },
    "narration": "Imagine you have limited time and money, but want to buy a new phone, go on vacation, and save for the future. You can't do everything."
  },
  {
    "t_start": 36.0,
    "t_end": 55.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "Because resources are scarce, we must make choices. Every decision involves giving something up to get something else.",
      "position": "bottom_right"
    },
    "narration": "This fundamental limitation forces individuals, businesses, and governments to make choices about how to allocate their resources."
  },
  {
    "t_start": 56.0,
    "t_end": 75.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "Opportunity Cost: The value of the next best alternative that was not taken when a decision was made due to scarcity.",
      "position": "center"
    },
    "narration": "And with every choice comes an opportunity cost \u2013 the value of what you gave up by choosing something else."
  },
  {
    "t_start": 76.0,
    "t_end": 95.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "If you spend your last $10 on a coffee, the opportunity cost might be the lunch you could have bought, or the savings you could have made.",
      "position": "top_right"
    },
    "narration": "For instance, if you choose to study for an exam, the opportunity cost might be the movie you missed with friends."
  },
  {
    "t_start": 96.0,
    "t_end": 115.0,
    "action": "SHOW_TEXT",
    "params": {
      "text": "Scarcity is a universal problem, affecting everyone from individuals to entire nations, driving all economic decisions.",
      "position": "bottom_left"
    },
    "narration": "Understanding scarcity and opportunity cost is key to understanding how economies function and why decisions are made."
  }
]
# To load beats from JSON instead:
# import json
# with open('basic-economics-problem-on-scarcity-20251026130648.json', 'r', encoding='utf-8') as fh:
#     BEATS = json.load(fh)

LABEL_POSITIONS = []
TEXT_POSITIONS = {
    'top_left': (1.2, 8.5),
    'top_right': (8.8, 8.5),
    'center': (5.0, 5.8),
    'bottom_left': (1.5, 1.5),
    'bottom_right': (8.5, 1.5),
}

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

def add_text_block(scene, axes, text, position):
    wrapped = textwrap.fill(text, width=48)
    lines = wrapped.split('\n') if wrapped else ['Economics']
    paragraph = Paragraph(*lines, alignment='left', line_spacing=0.8, font_size=34, color=BLACK)
    anchor = TEXT_POSITIONS.get(position, TEXT_POSITIONS['center'])
    paragraph.move_to(axes.c2p(*anchor))
    panel = SurroundingRectangle(paragraph, color=GRAY, buff=0.3, fill_opacity=0.05)
    block = VGroup(panel, paragraph)
    scene.play(FadeIn(block, shift=UP * 0.15), run_time=1.0)

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
            elif action == "SHOW_TEXT":
                add_text_block(
                    self,
                    axes,
                    params.get("text", "Economics insight"),
                    params.get("position", "center"),
                )
            self.wait(0.1)
