from manim import *

# Configure Manim for 1920x1080 resolution and 30 FPS
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class GeneratedScene(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # --- Introduction ---
        title = MathTex(r"\text{Understanding the Balance Sheet}", color=BLUE_D, font_size=72)
        self.play(Write(title))
        self.wait(1)

        definition_text = MathTex(
            r"\text{A financial statement that reports a company's assets, liabilities,}",
            r"\\ \text{and owner's equity at a specific point in time.}",
            color=BLACK, font_size=48
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=1)
        self.play(Write(definition_text[0]))
        self.play(Write(definition_text[1]))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(definition_text))
        self.wait(0.5)

        # --- The Accounting Equation ---
        equation_title = MathTex(r"\text{The Accounting Equation}", color=BLUE_D, font_size=64).to_edge(UP)
        self.play(Write(equation_title))
        self.wait(0.5)

        accounting_equation = MathTex(
            r"\text{Assets} = \text{Liabilities} + \text{Equity}",
            color=BLACK, font_size=72
        ).next_to(equation_title, DOWN, buff=1)
        self.play(Write(accounting_equation))
        self.wait(2)

        # Highlight components with distinct colors
        assets_text_highlight = accounting_equation[0:2].copy().set_color(GREEN_D)
        liabilities_text_highlight = accounting_equation[3:5].copy().set_color(RED_D)
        equity_text_highlight = accounting_equation[6:].copy().set_color(PURPLE_D)

        self.play(
            Transform(accounting_equation[0:2], assets_text_highlight),
            Transform(accounting_equation[3:5], liabilities_text_highlight),
            Transform(accounting_equation[6:], equity_text_highlight)
        )
        self.wait(1.5)

        self.play(FadeOut(equation_title), FadeOut(accounting_equation))
        self.wait(0.5)

        # --- Detailed Breakdown of Components ---
        components_title = MathTex(r"\text{Components of a Balance Sheet}", color=BLUE_D, font_size=64).to_edge(UP)
        self.play(Write(components_title))
        self.wait(1)

        # Assets Section
        assets_heading = MathTex(r"\text{1. Assets}", color=GREEN_D, font_size=56).to_edge(LEFT).shift(UP*1.5)
        assets_def = MathTex(r"\text{What a company owns.}", color=BLACK, font_size=40).next_to(assets_heading, DOWN, buff=0.3).align_to(assets_heading, LEFT)
        self.play(Write(assets_heading), Write(assets_def))
        self.wait(1)

        current_assets_title = MathTex(r"\text{Current Assets:}", color=GREEN_B, font_size=44).next_to(assets_def, DOWN, buff=0.5).align_to(assets_heading, LEFT)
        current_assets_list = VGroup(
            MathTex(r"\text{- Cash}", color=BLACK, font_size=36),
            MathTex(r"\text{- Accounts Receivable}", color=BLACK, font_size=36),
            MathTex(r"\text{- Inventory}", color=BLACK, font_size=36)
        ).arrange(DOWN, buff=0.2).next_to(current_assets_title, DOWN, buff=0.2).align_to(current_assets_title, LEFT)

        self.play(Write(current_assets_title))
        self.play(LaggedStart(*[Write(item) for item in current_assets_list], lag_ratio=0.5))
        self.wait(1)

        non_current_assets_title = MathTex(r"\text{Non-Current Assets:}", color=GREEN_B, font_size=44).next_to(current_assets_list, DOWN, buff=0.5).align_to(assets_heading, LEFT)
        non_current_assets_list = VGroup(
            MathTex(r"\text{- Property, Plant \& Equipment (PP\&E)}", color=BLACK, font_size=36),
            MathTex(r"\text{- Long-term Investments}", color=BLACK, font_size=36)
        ).arrange(DOWN, buff=0.2).next_to(non_current_assets_title, DOWN, buff=0.2).align_to(non_current_assets_title, LEFT)

        self.play(Write(non_current_assets_title))
        self.play(LaggedStart(*[Write(item) for item in non_current_assets_list], lag_ratio=0.5))
        self.wait(2)

        self.play(
            FadeOut(assets_heading), FadeOut(assets_def),
            FadeOut(current_assets_title), FadeOut(current_assets_list),
            FadeOut(non_current_assets_title), FadeOut(non_current_assets_list)
        )
        self.wait(0.5)

        # Liabilities Section
        liabilities_heading = MathTex(r"\text{2. Liabilities}", color=RED_D, font_size=56).to_edge(LEFT).shift(UP*1.5)
        liabilities_def = MathTex(r"\text{What a company owes to others.}", color=BLACK, font_size=40).next_to(liabilities_heading, DOWN, buff=0.3).align_to(liabilities_heading, LEFT)
        self.play(Write(liabilities_heading), Write(liabilities_def))
        self.wait(1)

        current_liabilities_title = MathTex(r"\text{Current Liabilities:}", color=RED_B, font_size=44).next_to(liabilities_def, DOWN, buff=0.5).align_to(liabilities_heading, LEFT)
        current_liabilities_list = VGroup(
            MathTex(r"\text{- Accounts Payable}", color=BLACK, font_size=36),
            MathTex(r"\text{- Salaries Payable}", color=BLACK, font_size=36),
            MathTex(r"\text{- Short-term Loans}", color=BLACK, font_size=36)
        ).arrange(DOWN, buff=0.2).next_to(current_liabilities_title, DOWN, buff=0.2).align_to(current_liabilities_title, LEFT)

        self.play(Write(current_liabilities_title))
        self.play(LaggedStart(*[Write(item) for item in current_liabilities_list], lag_ratio=0.5))
        self.wait(1)

        non_current_liabilities_title = MathTex(r"\text{Non-Current Liabilities:}", color=RED_B, font_size=44).next_to(current_liabilities_list, DOWN, buff=0.5).align_to(liabilities_heading, LEFT)
        non_current_liabilities_list = VGroup(
            MathTex(r"\text{- Long-term Debt}", color=BLACK, font_size=36),
            MathTex(r"\text{- Bonds Payable}", color=BLACK, font_size=36)
        ).arrange(DOWN, buff=0.2).next_to(non_current_liabilities_title, DOWN, buff=0.2).align_to(non_current_liabilities_title, LEFT)

        self.play(Write(non_current_liabilities_title))
        self.play(LaggedStart(*[Write(item) for item in non_current_liabilities_list], lag_ratio=0.5))
        self.wait(2)

        self.play(
            FadeOut(liabilities_heading), FadeOut(liabilities_def),
            FadeOut(current_liabilities_title), FadeOut(current_liabilities_list),
            FadeOut(non_current_liabilities_title), FadeOut(non_current_liabilities_list)
        )
        self.wait(0.5)

        # Equity Section
        equity_heading = MathTex(r"\text{3. Equity}", color=PURPLE_D, font_size=56).to_edge(LEFT).shift(UP*1.5)
        equity_def = MathTex(r"\text{The owners' claim on the assets.}", color=BLACK, font_size=40).next_to(equity_heading, DOWN, buff=0.3).align_to(equity_heading, LEFT)
        self.play(Write(equity_heading), Write(equity_def))
        self.wait(1)

        equity_components_title = MathTex(r"\text{Components:}", color=PURPLE_B, font_size=44).next_to(equity_def, DOWN, buff=0.5).align_to(equity_heading, LEFT)
        equity_components_list = VGroup(
            MathTex(r"\text{- Owner's Capital / Common Stock}", color=BLACK, font_size=36),
            MathTex(r"\text{- Retained Earnings}", color=BLACK, font_size=36)
        ).arrange(DOWN, buff=0.2).next_to(equity_components_title, DOWN, buff=0.2).align_to(equity_components_title, LEFT)

        self.play(Write(equity_components_title))
        self.play(LaggedStart(*[Write(item) for item in equity_components_list], lag_ratio=0.5))
        self.wait(2)

        self.play(
            FadeOut(components_title),
            FadeOut(equity_heading), FadeOut(equity_def),
            FadeOut(equity_components_title), FadeOut(equity_components_list)
        )
        self.wait(0.5)

        # --- Balance Sheet Structure (T-Account) ---
        structure_title = MathTex(r"\text{Balance Sheet Structure (T-Account)}", color=BLUE_D, font_size=64).to_edge(UP)
        self.play(Write(structure_title))
        self.wait(1)

        # Draw T-account lines
        vertical_line = Line(UP * 3.5, DOWN * 3.5, color=BLACK).shift(LEFT * 4)
        horizontal_line = Line(LEFT * 7, RIGHT * 7, color=BLACK).shift(UP * 2.5)
        self.play(Create(vertical_line), Create(horizontal_line))
        self.wait(0.5)

        assets_label = MathTex(r"\text{Assets}", color=GREEN_D, font_size=56).next_to(horizontal_line, UP, buff=0.5).shift(LEFT * 4)
        liabilities_equity_label = MathTex(r"\text{Liabilities + Equity}", color=BLUE_D, font_size=56).next_to(horizontal_line, UP, buff=0.5).shift(RIGHT * 4)
        self.play(Write(assets_label), Write(liabilities_equity_label))
        self.wait(1)

        # Placeholder for items in the T-account
        assets_items_label = MathTex(r"\text{Current Assets}", r"\\ \text{Non-Current Assets}", color=BLACK, font_size=40).next_to(assets_label, DOWN, buff=0.5).align_to(assets_label, LEFT)
        liabilities_items_label = MathTex(r"\text{Current Liabilities}", r"\\ \text{Non-Current Liabilities}", color=BLACK, font_size=40).next_to(liabilities_equity_label, DOWN, buff=0.5).align_to(liabilities_equity_label, LEFT)
        equity_items_label = MathTex(r"\text{Owner's Equity}", color=BLACK, font_size=40).next_to(liabilities_items_label, DOWN, buff=0.5).align_to(liabilities_equity_label, LEFT)

        self.play(Write(assets_items_label))
        self.play(Write(liabilities_items_label), Write(equity_items_label))
        self.wait(2)

        total_assets_label = MathTex(r"\text{Total Assets}", color=GREEN_D, font_size=48).next_to(vertical_line, DOWN, buff=0.5).shift(LEFT * 4)
        total_liabilities_equity_label = MathTex(r"\text{Total Liabilities \& Equity}", color=BLUE_D, font_size=48).next_to(vertical_line, DOWN, buff=0.5).shift(RIGHT * 4)
        self.play(Write(total_assets_label), Write(total_liabilities_equity_label))
        self.wait(1)

        balance_equation_final = MathTex(
            r"\text{Total Assets} = \text{Total Liabilities} + \text{Total Equity}",
            color=BLACK, font_size=56
        ).next_to(total_assets_label, DOWN, buff=1)
        self.play(Write(balance_equation_final))
        self.wait(3)

        self.play(
            FadeOut(structure_title), FadeOut(vertical_line), FadeOut(horizontal_line),
            FadeOut(assets_label), FadeOut(liabilities_equity_label),
            FadeOut(assets_items_label), FadeOut(liabilities_items_label), FadeOut(equity_items_label),
            FadeOut(total_assets_label), FadeOut(total_liabilities_equity_label),
            FadeOut(balance_equation_final)
        )
        self.wait(0.5)

        # --- Example 1: Simple Business Startup ---
        example1_title = MathTex(r"\text{Example 1: Simple Business Startup}", color=BLUE_D, font_size=64).to_edge(UP)
        self.play(Write(example1_title))
        self.wait(1)

        scenario1_text = MathTex(
            r"\text{John starts a business with \$10,000 cash (his capital).}",
            r"\\ \text{He then buys equipment for \$3,000 cash.}",
            color=BLACK, font_size=40
        ).arrange(DOWN, buff=0.5).next_to(example1_title, DOWN, buff=0.8)
        self.play(Write(scenario1_text[0]))
        self.wait(1.5)
        self.play(Write(scenario1_text[1]))
        self.wait(2)

        self.play(FadeOut(scenario1_text))
        self.wait(0.5)

        # Balance Sheet Table for Example 1
        bs_table_ex1_title = MathTex(r"\text{Balance Sheet (Example 1)}", color=BLUE_D, font_size=56).to_edge(UP)
        self.play(Transform(example1_title, bs_table_ex1_title)) # Transform the previous title
        self.wait(0.5)

        # Assets Section
        assets_header_ex1 = MathTex(r"\underline{\text{Assets}}", color=GREEN_D, font_size=48).to_edge(LEFT).shift(UP*2)
        cash_ex1 = MathTex(r"\text{Cash}", r"& \$7,000", color=BLACK, font_size=40).next_to(assets_header_ex1, DOWN, buff=0.5).align_to(assets_header_ex1, LEFT)
        equipment_ex1 = MathTex(r"\text{Equipment}", r"& \$3,000", color=BLACK, font_size=40).next_to(cash_ex1, DOWN, buff=0.3).align_to(assets_header_ex1, LEFT)
        total_assets_ex1 = MathTex(r"\underline{\underline{\text{Total Assets}}}", r"& \underline{\underline{\$10,000}}", color=GREEN_D, font_size=48).next_to(equipment_ex1, DOWN, buff=0.5).align_to(assets_header_ex1, LEFT)

        self.play(Write(assets_header_ex1))
        self.play(Write(cash_ex1))
        self.play(Write(equipment_ex1))
        self.play(Write(total_assets_ex1))
        self.wait(1)

        # Liabilities & Equity Section
        liabilities_equity_header_ex1 = MathTex(r"\underline{\text{Liabilities \& Equity}}", color=BLUE_D, font_size=48).next_to(assets_header_ex1, RIGHT, buff=4).align_to(assets_header_ex1, UP)
        liabilities_header_ex1 = MathTex(r"\text{Liabilities}", color=RED_D, font_size=40).next_to(liabilities_equity_header_ex1, DOWN, buff=0.5).align_to(liabilities_equity_header_ex1, LEFT)
        no_liabilities_ex1 = MathTex(r"\text{None}", r"& \$0", color=BLACK, font_size=40).next_to(liabilities_header_ex1, DOWN, buff=0.3).align_to(liabilities_equity_header_ex1, LEFT)
        
        equity_header_ex1 = MathTex(r"\text{Equity}", color=PURPLE_D, font_size=40).next_to(no_liabilities_ex1, DOWN, buff=0.5).align_to(liabilities_equity_header_ex1, LEFT)
        owners_capital_ex1 = MathTex(r"\text{Owner's Capital}", r"& \$10,000", color=BLACK, font_size=40).next_to(equity_header_ex1, DOWN, buff=0.3).align_to(liabilities_equity_header_ex1, LEFT)
        total_liabilities_equity_ex1 = MathTex(r"\underline{\underline{\text{Total Liabilities \& Equity}}}", r"& \underline{\underline{\$10,000}}", color=BLUE_D, font_size=48).next_to(owners_capital_ex1, DOWN, buff=0.5).align_to(liabilities_equity_header_ex1, LEFT)

        self.play(Write(liabilities_equity_header_ex1))
        self.play(Write(liabilities_header_ex1))
        self.play(Write(no_liabilities_ex1))
        self.play(Write(equity_header_ex1))
        self.play(Write(owners_capital_ex1))
        self.play(Write(total_liabilities_equity_ex1))
        self.wait(2)

        # Verify balance for Example 1
        balance_check_ex1 = MathTex(
            r"\text{Assets (\$10,000)} = \text{Liabilities (\$0)} + \text{Equity (\$10,000)}",
            color=BLACK, font_size=48
        ).next_to(total_assets_ex1, DOWN, buff=1.5).shift(RIGHT*2)
        self.play(Write(balance_check_ex1))
        self.wait(3)

        self.play(
            FadeOut(example1_title), FadeOut(assets_header_ex1), FadeOut(cash_ex1), FadeOut(equipment_ex1), FadeOut(total_assets_ex1),
            FadeOut(liabilities_equity_header_ex1), FadeOut(liabilities_header_ex1), FadeOut(no_liabilities_ex1),
            FadeOut(equity_header_ex1), FadeOut(owners_capital_ex1), FadeOut(total_liabilities_equity_ex1),
            FadeOut(balance_check_ex1)
        )
        self.wait(0.5)

        # --- Example 2: Impact of a Transaction ---
        example2_title = MathTex(r"\text{Example 2: Impact of a Transaction}", color=BLUE_D, font_size=64).to_edge(UP)
        self.play(Write(example2_title))
        self.wait(1)

        # Display Initial Balance Sheet (from Example 1)
        initial_bs_title = MathTex(r"\text{Initial Balance Sheet}", color=BLUE_D, font_size=48).next_to(example2_title, DOWN, buff=0.8)
        self.play(Write(initial_bs_title))
        self.wait(0.5)

        initial_assets = VGroup(
            MathTex(r"\text{Cash: \$7,000}", color=BLACK, font_size=36),
            MathTex(r"\text{Equipment: \$3,000}", color=BLACK, font_size=36),
            MathTex(r"\text{Total Assets: \$10,000}", color=GREEN_D, font_size=36)
        ).arrange(DOWN, buff=0.3).next_to(initial_bs_title, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        initial_liabilities_equity = VGroup(
            MathTex(r"\text{Liabilities: \$0}", color=RED_D, font_size=36),
            MathTex(r"\text{Owner's Capital: \$10,000}", color=PURPLE_D, font_size=36),
            MathTex(r"\text{Total L\&E: \$10,000}", color=BLUE_D, font_size=36)
        ).arrange(DOWN, buff=0.3).next_to(initial_bs_title, DOWN, buff=0.5).to_edge(RIGHT, buff=1)

        self.play(Write(initial_assets), Write(initial_liabilities_equity))
        self.wait(2)

        transaction_text = MathTex(
            r"\text{Transaction: The business buys \$2,000 worth of inventory on credit.}",
            color=BLACK, font_size=40
        ).next_to(initial_assets, DOWN, buff=1).shift(RIGHT*0.5)
        self.play(Write(transaction_text))
        self.wait(2)

        # Clear initial balance sheet to make space for the updated one
        self.play(FadeOut(initial_assets), FadeOut(initial_liabilities_equity))
        self.wait(0.5)

        # Updated Balance Sheet
        updated_bs_title = MathTex(r"\text{Updated Balance Sheet}", color=BLUE_D, font_size=48).next_to(example2_title, DOWN, buff=0.8)
        self.play(Transform(initial_bs_title, updated_bs_title)) # Transform the previous title
        self.wait(0.5)

        # Assets
        updated_assets_header = MathTex(r"\underline{\text{Assets}}", color=GREEN_D, font_size=48).to_edge(LEFT).shift(UP*2)
        updated_cash = MathTex(r"\text{Cash}", r"& \$7,000", color=BLACK, font_size=40).next_to(updated_assets_header, DOWN, buff=0.5).align_to(updated_assets_header, LEFT)
        updated_equipment = MathTex(r"\text{Equipment}", r"& \$3,000", color=BLACK, font_size=40).next_to(updated_cash, DOWN, buff=0.3).align_to(updated_assets_header, LEFT)
        updated_inventory = MathTex(r"\text{Inventory}", r"& \$2,000", color=BLACK, font_size=40).next_to(updated_equipment, DOWN, buff=0.3).align_to(updated_assets_header, LEFT) # New item
        updated_total_assets = MathTex(r"\underline{\underline{\text{Total Assets}}}", r"& \underline{\underline{\$12,000}}", color=GREEN_D, font_size=48).next_to(updated_inventory, DOWN, buff=0.5).align_to(updated_assets_header, LEFT)

        self.play(Write(updated_assets_header))
        self.play(Write(updated_cash))
        self.play(Write(updated_equipment))
        self.play(Write(updated_inventory)) 
        self.play(Write(updated_total_assets))
        self.wait(1)

        # Liabilities & Equity
        updated_liabilities_equity_header = MathTex(r"\underline{\text{Liabilities \& Equity}}", color=BLUE_D, font_size=48).next_to(updated_assets_header, RIGHT, buff=4).align_to(updated_assets_header, UP)
        updated_liabilities_header = MathTex(r"\text{Liabilities}", color=RED_D, font_size=40).next_to(updated_liabilities_equity_header, DOWN, buff=0.5).align_to(updated_liabilities_equity_header, LEFT)
        updated_accounts_payable = MathTex(r"\text{Accounts Payable}", r"& \$2,000", color=BLACK, font_size=40).next_to(updated_liabilities_header, DOWN, buff=0.3).align_to(updated_liabilities_equity_header, LEFT) # New item
        
        updated_equity_header = MathTex(r"\text{Equity}", color=PURPLE_D, font_size=40).next_to(updated_accounts_payable, DOWN, buff=0.5).align_to(updated_liabilities_equity_header, LEFT)
        updated_owners_capital = MathTex(r"\text{Owner's Capital}", r"& \$10,000", color=BLACK, font_size=40).next_to(updated_equity_header, DOWN, buff=0.3).align_to(updated_liabilities_equity_header, LEFT)
        updated_total_liabilities_equity = MathTex(r"\underline{\underline{\text{Total Liabilities \& Equity}}}", r"& \underline{\underline{\$12,000}}", color=BLUE_D, font_size=48).next_to(updated_owners_capital, DOWN, buff=0.5).align_to(updated_liabilities_equity_header, LEFT)

        self.play(Write(updated_liabilities_equity_header))
        self.play(Write(updated_liabilities_header))
        self.play(Write(updated_accounts_payable)) 
        self.play(Write(updated_equity_header))
        self.play(Write(updated_owners_capital))
        self.play(Write(updated_total_liabilities_equity))
        self.wait(2)

        # Verify balance again for Example 2
        balance_check_ex2 = MathTex(
            r"\text{Assets (\$12,000)} = \text{Liabilities (\$2,000)} + \text{Equity (\$10,000)}",
            color=BLACK, font_size=48
        ).next_to(updated_total_assets, DOWN, buff=1.5).shift(RIGHT*2)
        self.play(Write(balance_check_ex2))
        self.wait(3)

        self.play(
            FadeOut(example2_title), FadeOut(initial_bs_title), FadeOut(transaction_text),
            FadeOut(updated_assets_header), FadeOut(updated_cash), FadeOut(updated_equipment), FadeOut(updated_inventory), FadeOut(updated_total_assets),
            FadeOut(updated_liabilities_equity_header), FadeOut(updated_liabilities_header), FadeOut(updated_accounts_payable),
            FadeOut(updated_equity_header), FadeOut(updated_owners_capital), FadeOut(updated_total_liabilities_equity),
            FadeOut(balance_check_ex2)
        )
        self.wait(0.5)

        # --- Conclusion ---
        conclusion_title = MathTex(r"\text{Key Takeaways}", color=BLUE_D, font_size=72)
        self.play(Write(conclusion_title))
        self.wait(1)

        takeaways = VGroup(
            MathTex(r"\text{- Snapshot of financial health at a point in time.}", color=BLACK, font_size=48),
            MathTex(r"\text{- Always balances: Assets = Liabilities + Equity.}", color=BLACK, font_size=48),
            MathTex(r"\text{- Essential for understanding a company's financial position.}", color=BLACK, font_size=48)
        ).arrange(DOWN, buff=0.8).next_to(conclusion_title, DOWN, buff=1)

        self.play(LaggedStart(*[Write(item) for item in takeaways], lag_ratio=0.7))
        self.wait(4)

        self.play(FadeOut(conclusion_title), FadeOut(takeaways))
        self.wait(1)