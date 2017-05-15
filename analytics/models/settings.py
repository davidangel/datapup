from analytics.config import Config

file_names = {
    'petsafe': {
        'voc': 'data/PetSafeVOCSurvey.csv',
        'cc': 'data/PetSafeFeedbackCommentCard.csv'
    },
    'sportdog': {
        'voc': 'data/SportDOGVOCSurvey.csv',
        'cc': 'data/SportDOGFeedbackCommentCard.csv'
    }
}

column_rename = {
    Config.PETSAFE_APP: {
        Config.VOC_SURVEY: {
            'StartDate': 'StartDate',
            'EndDate': 'EndDate',
            'Progress': 'Progress',
            'Duration (in seconds)': 'Duration(seconds)',
            'Finished': 'Finished',
            'LocationLatitude': 'LocationLatitude',
            'LocationLongitude': 'LocationLongitude',
            'Q17': 'FeedbackType',
            'Q2_1': 'WebsiteRating',
            'Q3': 'PurposeSelect',
            'Q3_6_TEXT': 'PurposeText',
            'Q5': 'CompletedPurpose',
            'Q6': 'WhyNotCompletedPurpose',
            'Q7': 'ValueAboutWebsite',
            'Q8': 'ProductRating',
            'Q18': 'ProductRatingDescription',
            'Q11_1': 'Email',
            'Q16_Browser': 'Browser',
            'Q16_Operating System': 'OperatingSystem',
            'Q16_Resolution': 'Resolution',
            'Referer': 'Referrer',
        },
        Config.COMMENT_CARD_SURVEY: {
            'StartDate': 'StartDate',
            'EndDate': 'EndDate',
            'Progress': 'Progress',
            'Duration (in seconds)': 'Duration(seconds)',
            'Finished': 'Finished',
            'LocationLatitude': 'LocationLatitude',
            'LocationLongitude': 'LocationLongitude',
            'Q11': 'FeedbackType',
            'Q1': 'FeedbackCategory',
            'Q2': 'SuggestionText',
            'Q3': 'DislikeText',
            'Q4': 'PraiseText',
            'Q5_1': 'WebsiteRating',
            'Q12': 'ProductRating',
            'Q14': 'ProductRatingDescription',
            'Q6_1': 'Email',
            'Q8_Browser': 'Browser',
            'Q8_Operating System': 'OperatingSystem',
            'Q8_Resolution': 'Resolution',
            'Referer': 'Referrer',
        }
    },
    Config.SPORTDOG_APP: {
        Config.VOC_SURVEY: {
            'StartDate': 'StartDate',
            'EndDate': 'EndDate',
            'Progress': 'Progress',
            'Duration (in seconds)': 'Duration(seconds)',
            'Finished': 'Finished',
            'LocationLatitude': 'LocationLatitude',
            'LocationLongitude': 'LocationLongitude',
            'Q16': 'FeedbackType',
            'Q2_1': 'WebsiteRating',
            'Q3': 'PurposeSelect',
            'Q3_6_TEXT': 'PurposeText',
            'Q5': 'CompletedPurpose',
            'Q6': 'WhyNotCompletedPurpose',
            'Q7': 'ValueAboutWebsite',
            'Q8': 'ProductRating',
            'Q15': 'ProductRatingDescription',
            'Q11_1': 'Email',
            'Q16_Browser': 'Browser',
            'Q16_Operating System': 'OperatingSystem',
            'Q16_Resolution': 'Resolution',
            'Referer': 'Referrer',
        },
        Config.COMMENT_CARD_SURVEY: {
            'StartDate': 'StartDate',
            'EndDate': 'EndDate',
            'Progress': 'Progress',
            'Duration (in seconds)': 'Duration(seconds)',
            'Finished': 'Finished',
            'LocationLatitude': 'LocationLatitude',
            'LocationLongitude': 'LocationLongitude',
            'Q11': 'FeedbackType',
            'Q1': 'FeedbackCategory',
            'Q2': 'SuggestionText',
            'Q3': 'DislikeText',
            'Q4': 'PraiseText',
            'Q5': 'ProductRating',
            'Q6_1': 'Email',
            'Q8_Browser': 'Browser',
            'Q8_Operating System': 'OperatingSystem',
            'Q8_Resolution': 'Resolution',
            'Referer': 'Referrer',
        }
    }
}

column_types = {
    'StartDate': 'datetime64',
    'EndDate': 'datetime64',
    'Progress': 'int64',
    'Duration(seconds)': 'int64',
    'Finished': 'bool',
    'LocationLatitude': 'object',
    'LocationLongitude': 'object',
    'FeedbackType': 'object',
    'WebsiteRating': 'object',
    'PurposeSelect': 'object',
    'PurposeText': 'object',
    'CompletedPurpose': 'bool',
    'WhyNotCompletedPurpose': 'object',
    'ValueAboutWebsite': 'object',
    'ProductRating': 'int64',
    'ProductRatingDescription': 'object',
    'Email': 'object',
    'Browser': 'object',
    'OperatingSystem': 'object',
    'Resolution': 'object',
    'Referrer': 'object',
    'FeedbackCategory': 'object',
    'SuggestionText': 'object',
    'DislikeText': 'object',
    'PraiseText': 'object',
}

column_scale = {
    'WebsiteRating': {
            'Very Bad': 1,
            'Bad': 1,
            'Fair': 2,
            'Good': 3,
            'Very Good': 3,
            'Default': 0
        },
    'ProductRating': {
        '0': 1,
        '1': 1,
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1,
        '7': 2,
        '8': 2,
        '9': 3,
        '10': 3,
        'Default': 0
    }
}
