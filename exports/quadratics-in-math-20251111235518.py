from manim import *

# Configure global settings for the scene
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30


class GeneratedScene(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # --- Title ---
        title = Text("Quadratics", font_size=96, color=BLACK).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- Introduction ---
        intro_text = Text(
            "Equations and functions involving a squared variable.",
            font_size=48,
            color=BLACK,
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # --- Standard Form ---
        standard_form_title = Text("Standard Form:", font_size=60, color=BLACK).to_edge(
            UP
        )
        self.play(Transform(title, standard_form_title))

        equation = MathTex("ax^2 + bx + c = 0", font_size=96, color=BLUE).center()
        self.play(Write(equation))
        self.wait(1)

        a_text = MathTex("a \\neq 0", font_size=48, color=RED).next_to(
            equation, DOWN, buff=0.5
        )
        abc_text = Text("a, b, c are constants", font_size=48, color=BLACK).next_to(
            a_text, DOWN
        )
        self.play(Write(a_text), Write(abc_text))
        self.wait(2)
        self.play(FadeOut(equation), FadeOut(a_text), FadeOut(abc_text))

        # --- Graphical Representation: The Parabola ---
        graph_title = Text(
            "Graphical Representation: The Parabola", font_size=60, color=BLACK
        ).to_edge(UP)
        self.play(Transform(title, graph_title))

        # Setup axes
        axes = (
            Axes(
                x_range=[-4, 4, 1],
                y_range=[-4, 4, 1],
                x_length=8,
                y_length=8,
                axis_config={"color": GRAY_B, "stroke_width": 2},
            )
            .center()
            .add_coordinates()
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Plot a generic parabola
        parabola_func = lambda x: 0.5 * x**2 - 2
        parabola = axes.get_graph(parabola_func, color=BLUE, stroke_width=4)
        parabola_label = (
            MathTex("y = ax^2 + bx + c", font_size=40, color=BLUE)
            .next_to(parabola, UP, buff=0.5)
            .shift(RIGHT * 1.5)
        )
        self.play(Create(parabola), Write(parabola_label))
        self.wait(2)

        # --- Key Features ---
        features_title = Text(
            "Key Features of a Parabola", font_size=60, color=BLACK
        ).to_edge(UP)
        self.play(Transform(title, features_title))
        self.play(FadeOut(parabola_label))

        # Vertex
        vertex_point = axes.coords_to_point(0, -2)
        vertex_dot = Dot(vertex_point, color=RED, radius=0.1)
        vertex_label = (
            Text("Vertex (Min/Max Point)", font_size=36, color=RED)
            .next_to(vertex_dot, RIGHT, buff=0.5)
            .shift(UP * 0.2)
        )
        self.play(FadeIn(vertex_dot), Write(vertex_label))
        self.wait(1.5)

        # Axis of Symmetry
        axis_of_sym = axes.get_vertical_line(
            axes.coords_to_point(0, 0),
            color=GREEN,
            line_arg={"stroke_width": 3, "dash_length": 0.1},
        )
        axis_sym_label = (
            Text("Axis of Symmetry", font_size=36, color=GREEN)
            .next_to(axis_of_sym, UP, buff=0.5)
            .shift(LEFT * 0.5)
        )
        self.play(Create(axis_of_sym), Write(axis_sym_label))
        self.wait(1.5)

        # Roots/X-intercepts
        root1_point = axes.coords_to_point(-2, 0)
        root2_point = axes.coords_to_point(2, 0)
        root_dots = VGroup(
            Dot(root1_point, color=PURPLE, radius=0.1),
            Dot(root2_point, color=PURPLE, radius=0.1),
        )
        roots_label = (
            Text("Roots / X-intercepts (where y=0)", font_size=36, color=PURPLE)
            .next_to(root_dots, DOWN, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(FadeIn(root_dots), Write(roots_label))
        self.wait(2)

        # Clear features
        self.play(
            FadeOut(vertex_dot),
            FadeOut(vertex_label),
            FadeOut(axis_of_sym),
            FadeOut(axis_sym_label),
            FadeOut(root_dots),
            FadeOut(roots_label),
        )
        self.wait(0.5)

        # --- Example: y = x^2 - 4 ---
        example_title = Text("Example: y = x^2 - 4", font_size=60, color=BLACK).to_edge(
            UP
        )
        self.play(Transform(title, example_title))
        self.play(FadeOut(parabola))  # Fade out the generic parabola
        self.wait(0.5)

        # Plotting the specific example parabola
        example_func = lambda x: x**2 - 4
        example_parabola = axes.get_graph(example_func, color=ORANGE, stroke_width=4)
        example_parabola_label = (
            MathTex("y = x^2 - 4", font_size=40, color=ORANGE)
            .next_to(example_parabola, UP, buff=0.5)
            .shift(RIGHT * 1.5)
        )
        self.play(Create(example_parabola), Write(example_parabola_label))
        self.wait(1)

        # Highlight features for the example
        # Vertex
        ex_vertex_point = axes.coords_to_point(0, -4)
        ex_vertex_dot = Dot(ex_vertex_point, color=RED, radius=0.1)
        ex_vertex_label = (
            Text("Vertex (0, -4)", font_size=36, color=RED)
            .next_to(ex_vertex_dot, RIGHT, buff=0.5)
            .shift(UP * 0.2)
        )
        self.play(FadeIn(ex_vertex_dot), Write(ex_vertex_label))
        self.wait(1.5)

        # Roots
        ex_root1_point = axes.coords_to_point(-2, 0)
        ex_root2_point = axes.coords_to_point(2, 0)
        ex_root_dots = VGroup(
            Dot(ex_root1_point, color=PURPLE, radius=0.1),
            Dot(ex_root2_point, color=PURPLE, radius=0.1),
        )
        ex_roots_label = (
            Text("Roots (-2, 0) and (2, 0)", font_size=36, color=PURPLE)
            .next_to(ex_root_dots, DOWN, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(FadeIn(ex_root_dots), Write(ex_roots_label))
        self.wait(2)

        # Clear example features
        self.play(
            FadeOut(ex_vertex_dot),
            FadeOut(ex_vertex_label),
            FadeOut(ex_root_dots),
            FadeOut(ex_roots_label),
            FadeOut(example_parabola_label),
        )
        self.wait(0.5)

        # --- Conclusion ---
        self.play(FadeOut(example_parabola), FadeOut(axes), FadeOut(labels))
        conclusion_text = Text(
            "Quadratics are fundamental in various fields of science and engineering!",
            font_size=48,
            color=BLACK,
        ).center()
        self.play(Transform(title, Text("Conclusion", font_size=96, color=BLACK).to_edge(UP)))
        self.play(Write(conclusion_text))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(conclusion_text))
        self.wait(1)