import pymol
pymol.finish_launching()

# List of PDB IDs to fetch
pdb_ids = ['6HPJ', '6I1M', '6I45', '6IVH', '6IZG', '6J4C', '6J6V', '6JEC', '6JHE', '6JPD', '6JPP', '6JTF', '6JUE', '6JUI', '6JV8','6JVX', '6JVY', '6JXU', '6JXV', '6JXW', '6JXX', '6K5W', '6K7W', '6K9I', '6KCU', '6KGI', '6KHV', '6KIL', '6KKP', '6KOL','6KQV', '6KYX', '6KZ1', '6L0O', '6L2A', '6L7Z', '6L9S', '6LCB', '6LCQ', '6LJI', '6LLQ', '6LMR', '6LP4', '6LSQ', '6LU6','6LWZ', '6LXL', '6LZP', '6M1B', '6M1U', '6M1V', '6M3A', '6M4C', '6M6E', '6M6F', '6NU0', '6O40', '6O8K', '6O8L', '6O8M','6OGL', '6OGP', '6OGQ', '6OGR', '6OGS', '6OGT', '6OGV', '6OJ7', '6OSN', '6OYD', '6OYR', '6P1Y', '6Q2I', '6QAY', '6QBI','6QS0', '6R1L', '6RCC', '6RJU', '6RSN', '6S92', '6SA4', '6SA5', '6SI6', '6SLY', '6SPT', '6ST4', '6ST6', '6ST7', '6STC','6SYJ', '6T2E', '6T2F', '6T36', '6TDD', '6TDM', '6TG5', '6TGS', '6TGY', '6TM6', '6TN7', '6TNE', '6TO5', '6TO9', '6TOC','6TPB', '6TRJ', '6TVU', '6TY2', '6TZE', '6U6R', '6U6S', '6U97', '6U9P', '6U9T', '6U9Z', '6UGC', '6UT2', '6UTC', '6UUE','6UY7', '6V0X', '6V14', '6V1W', '6V4F', '6V4G', '6V67', '6V7U', '6VAS', '6VDA', '6VG7', '6VGA', '6VGB', '6VHI', '6VJ0','6VJG', '6VJO', '6VK2', '6VLP', '6VMT', '6VRJ', '6VSI', '6VSK', '6VWB', '6VZ6', '6VZF', '6W2G', '6W3W', '6W46', '6W74','6W8E', '6W9Q', '6W9Y', '6WA3', '6WA4', '6WA5', '6WBE', '6WBU', '6WI6', '6WW4', '6WZC', '6X1K', '6X1N', '6X1P', '6X1R','6X1X', '6X20', '6X22', '6X23', '6X38', '6X39', '6X8X', '6X9Z', '6XAW', '6XFK', '6XFL', '6XMN', '6XNE', '6XNF', '6XNJ','6XNL', '6XNM', '6XPK', '6XPL', '6XTT', '6XUO', '6XZ3', '6Y06', '6Y3Q', '6Y96', '6Y9N', '6Y9O', '6Y9Q', '6YB1', '6YE5','6YEL', '6YET', '6YEU', '6YFY', '6YIG', '6YJ0', '6YJD', '6YPI', '6YPR', '6YTU', '6Z1W', '6Z29', '6Z2G', '6Z35', '6Z5N','6Z5W', '6Z5X', '6Z5Z', '6Z60', '6Z7O', '6ZC6', '6ZCT', '6ZDY', '6ZE9', '6ZFE', '6ZGN', '6ZHB', '6ZI0', '6ZI8', '6ZIL','6ZNB', '6ZOM', '6ZSO', '6ZUM', '6ZV0', '6ZV3', '6ZV4', '6ZYG', '7A0I', '7A2L', '7A2W', '7A2X', '7A2Y', '7A39', '7A3D','7A6X', '7AAO', '7AEP', '7AFQ', '7AH0', '7AH2', '7AHT', '7AHY', '7AKT', '7AL1', '7AL2', '7AQT', '7ARS', '7ASW', '7ATH','7ATK', '7AUF', '7AV6', '7AVJ', '7AX5', '7B21', '7B5W', '7B76', '7B7J', '7B9X', '7BB3', '7BBQ', '7BC2', '7BIR', '7BIT','7BIV', '7BJ6', '7BJG', '7BJN', '7BK5', '7BL8', '7BLB', '7BLC', '7BLD', '7BMG', '7BMV', '7BMW', '7BMZ', '7BNP', '7BPL','7BPP', '7BQB', '7BQD', '7BQE', '7BQF', '7BQG', '7BQM', '7BQN', '7BQS', '7BSO', '7BUH', '7BXY', '7BZD', '7BZE', '7C00','7C20', '7C21', '7C28', '7C31', '7C3Q', '7C3Y', '7C3Z', '7C44', '7C4O', '7CFZ', '7CG5', '7CHQ', '7CHR', '7CJV', '7CJW','7CLT', '7CNB', '7CNF', '7CPZ', '7CQF', '7CQP', '7CRE', '7CT3', '7CWK', '7CX5', '7CY1', '7CZ6', '7CZO', '7D35', '7D4A','7DDA', '7DES', '7DG7', '7DG9', '7DGU', '7DGW', '7DGX', '7DGY', '7DH4', '7DHB', '7DHT', '7DIO', '7DIQ', '7DIS', '7DIU','7DIZ', '7DMS', '7DPO', '7DPX', '7DSG', '7DTA', '7DU6', '7DUF', '7DVF', '7DXX', '7DXY', '7DY0', '7E0B', '7E8L', '7EFY','7EK6', '7EL4', '7EPG', '7EPI', '7EPJ', '7EQ4', '7ET5', '7EUA', '7EYJ', '7EYK', '7F0N', '7F3K', '7F3L', '7F5F', '7F7X','7FAX', '7FBR', '7FBV', '7FC7']


# Fetch each PDB file
for pdb_id in pdb_ids:
    pymol.cmd.fetch(pdb_id, type='pdb')

# Optional: save each fetched structure as a file
for pdb_id in pdb_ids:
    pymol.cmd.save(f"{pdb_id}.pdb", pdb_id)

pymol.cmd.quit()