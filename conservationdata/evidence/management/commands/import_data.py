import openpyxl
from django.core.management.base import BaseCommand
from evidence.models import Evidence
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Import conservation evidence data from an Excel (.xlsx) file with validation.'

    VALID_EVIDENCE_TYPES = {'Experimental', 'Observational', 'Review'}

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['excel_file']

        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active

            count = 0
            for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                title, species, year, location, score, evidence_type, outcome = row

                # # Validate year
                # if not isinstance(year, int) or not (1000 <= year <= 2100):
                #     self.stderr.write(f"Row {i} skipped: Invalid year '{year}'")
                #     continue

                # Validate score
                # if not isinstance(score, int) or not (1 <= score <= 5):
                #     self.stderr.write(f"Row {i} skipped: Invalid effectiveness score '{score}'")
                #     continue


                # Validate evidence type
                if evidence_type not in self.VALID_EVIDENCE_TYPES:
                    self.stderr.write(f"Row {i} skipped: Unknown evidence type '{evidence_type}'")
                    continue

                try:
                    Evidence.objects.create(
                        intervention_title=title,
                        species_group=species,
                        year=year,
                        location=location,
                        effectiveness_score=score,
                        evidence_type=evidence_type,
                        brief_outcome=outcome
                    )
                    count += 1
                except Exception as e:
                    self.stderr.write(f"Row {i} skipped on save: {e}")

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {count} valid records."))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error processing file: {e}"))
