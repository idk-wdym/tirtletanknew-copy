from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # --- Configuration ---
        # Set pixel resolution for the output video to 1920x1080
        config.pixel_width = 1920
        config.pixel_height = 1080
        # Set frame rate to 30 frames per second
        config.frame_rate = 30
        # Set background color to white
        self.camera.background_color = WHITE

        # --- 1. Title ---
        title = Text("Opportunity Cost", font_size=96, color=BLACK)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP).scale(0.7))

        # --- 2. Definition ---
        definition_text = Text(
            "The value of the next best alternative that was not chosen.",
            font_size=48,
            color=BLACK,
            wrap_width=config.frame_width - 2 # Ensure text fits horizontally within the frame
        )
        definition_text.next_to(title, DOWN, buff=0.8)
        self.play(Write(definition_text))
        self.wait(2)
        self.play(FadeOut(definition_text))

        # --- 3. Scenario Setup ---
        # Introduce the resource or decision-maker
        resource_text = Text("You have $5", font_size=64, color=BLUE_E)
        self.play(Write(resource_text))
        self.wait(1)

        # Option 1: Buy Coffee
        option_coffee_label = Text("Buy Coffee", font_size=48, color=BLACK)
        coffee_icon = Text("☕", font_size=72, color=BROWN) # Using Unicode emoji for visual representation
        option_coffee_group = VGroup(coffee_icon, option_coffee_label).arrange(DOWN, buff=0.3)
        option_coffee_box = RoundedRectangle(
            width=4, height=3, corner_radius=0.5, color=BLUE, fill_opacity=0.1
        ).surround(option_coffee_group, buff=0.5)
        option_coffee = VGroup(option_coffee_box, option_coffee_group)
        option_coffee.shift(LEFT * 4)

        # Option 2: Save for Book
        option_book_label = Text("Save for Book", font_size=48, color=BLACK)
        book_icon = Text("📚", font_size=72, color=GREEN_E) # Using Unicode emoji for visual representation
        option_book_group = VGroup(book_icon, option_book_label).arrange(DOWN, buff=0.3)
        option_book_box = RoundedRectangle(
            width=4, height=3, corner_radius=0.5, color=GREEN, fill_opacity=0.1
        ).surround(option_book_group, buff=0.5)
        option_book = VGroup(option_book_box, option_book_group)
        option_book.shift(RIGHT * 4)

        self.play(
            resource_text.animate.shift(UP * 2), # Move resource text up to make space for options
            FadeIn(option_coffee, shift=LEFT),   # Fade in coffee option from the left
            FadeIn(option_book, shift=RIGHT)     # Fade in book option from the right
        )
        self.wait(1.5)

        # --- 4. Making a Choice ---
        choice_arrow = Arrow(
            start=resource_text.get_bottom(),
            end=option_coffee_box.get_top(),
            buff=0.1,
            color=BLUE_D,
            stroke_width=8
        )
        choice_text = Text("You choose...", font_size=40, color=BLACK).next_to(choice_arrow, UP)

        self.play(
            Create(choice_arrow),
            Write(choice_text),
            option_coffee_box.animate.set_fill(BLUE, opacity=0.4), # Highlight the chosen option
            run_time=1.5
        )
        self.wait(1)
        self.play(FadeOut(choice_text), FadeOut(resource_text)) # The resource is now allocated

        # --- 5. Highlighting Opportunity Cost ---
        # The book option is the opportunity cost (the foregone alternative)
        opportunity_cost_label = Text("Opportunity Cost", font_size=60, color=RED_E)
        opportunity_cost_label.next_to(option_book, UP, buff=1)

        # Arrow pointing to the foregone option
        oc_arrow = Arrow(
            start=opportunity_cost_label.get_bottom(),
            end=option_book_box.get_top(),
            buff=0.1,
            color=RED_E,
            stroke_width=8
        )

        self.play(
            FadeIn(opportunity_cost_label, shift=UP),
            Create(oc_arrow),
            option_book_box.animate.set_fill(RED, opacity=0.4), # Highlight the foregone option
            run_time=1.5
        )
        self.wait(2)

        # --- 6. Conclusion ---
        conclusion_text = Text(
            "By choosing coffee, you gave up the opportunity to save for a book.",
            font_size=48,
            color=BLACK,
            wrap_width=config.frame_width - 2
        )
        conclusion_text.move_to(DOWN * 3)

        self.play(
            FadeOut(choice_arrow),
            FadeOut(option_coffee), # Fade out the chosen option as it's no longer the focus
            FadeOut(oc_arrow),
            FadeOut(opportunity_cost_label),
            option_book.animate.move_to(UP * 0.5), # Move the foregone option to center for emphasis
            Write(conclusion_text)
        )
        self.wait(3)
        self.play(FadeOut(self.mobjects)) # Clear all remaining mobjects from the scene