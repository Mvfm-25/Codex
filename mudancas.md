@Test
    @DisplayName("updateQuizQuestion should update question successfully")
    void updateQuizQuestionShouldUpdateQuestionSuccessfully() {
        QuizQuestion quizQuestion = questionEntities.get(0);
        QuizQuestionResponseDto quizQuestionDto = questionsDtos.get(0);
        when(quizQuestionRepository.findById(1L)).thenReturn(Optional.of(quizQuestion));
        when(quizQuestionMapper.toDto(quizQuestion)).thenReturn(quizQuestionDto);

        QuizQuestionResponseDto result = quizQuestionService.updateQuizQuestion(1L, quizQuestionDto);
        assertNotNull(result);
        assertEquals("Question 1", result.question());

        verify(quizQuestionRepository, times(1)).findById(1L);
        verify(quizQuestionRepository, times(1)).save(any(QuizQuestion.class));
        verify(quizQuestionMapper, times(1)).toDto(any(QuizQuestion.class));
    }
